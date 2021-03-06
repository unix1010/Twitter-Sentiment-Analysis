from svmutil import *

def svmClassifierModel(trainingLabel, featureVectorsTrain, modelPath):
    
    """Feed the feature vector to svm to create model"""
    print "Creating SVM Model"
    model= svm_train(trainingLabel,featureVectorsTrain)
    print "Model created. Saving..."

    """Save model"""
    svm_save_model(modelPath, model)
    print "Model Saved. Proceed to test..."
    return

def svmLabelPredicter(testingLabel,featureVectorsTest,modelPath):
    
    """Load Model"""
    print "Loading Model"
    model= svm_load_model(modelPath)

    predictedLabel, predictedAcc, predictedValue = svm_predict(testingLabel, featureVectorsTest, model)
    print "Finished. The accuracy is:"
    print predictedAcc[0]
    return predictedLabel
