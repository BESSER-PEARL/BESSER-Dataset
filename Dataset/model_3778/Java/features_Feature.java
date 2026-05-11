





import java.util.List;
import java.util.ArrayList;

public class features_Feature  {

    private boolean mandatory;
    private String nome;





    private features_Root features_root;




    private features_Feature features_feature;


    public features_Feature(
        boolean mandatory,        String nome    ) {
        this.mandatory = mandatory;
        this.nome = nome;
    }


    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public features_Root getFeatures_root() {
        return features_root;
    }

    public void setFeatures_root(features_Root features_root) {
        this.features_root = features_root;
    }
    public features_Feature getFeatures_feature() {
        return features_feature;
    }

    public void setFeatures_feature(features_Feature features_feature) {
        this.features_feature = features_feature;
    }

}