import numpy as np
import pickle
import joblib

class Model:
    
    def carrega_modelo(self,path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um apanhado com base no modelo treinado
        """
        X_input = np.array([ 
                            form.age, 
                            form.gender,
                            form.height,
                            form.weight,
                            form.ap_hi,
                            form.ap_lo,
                            form.cholesterol
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])