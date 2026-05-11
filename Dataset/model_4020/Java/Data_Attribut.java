





import java.util.List;
import java.util.ArrayList;

public class Data_Attribut  {

    private String typeStr;
    private String nom;
    private boolean estTableau;





    private Data_Classe data_classe;




    private Data_Classe data_classe;


    public Data_Attribut(
        String typeStr,        String nom,        boolean estTableau    ) {
        this.typeStr = typeStr;
        this.nom = nom;
        this.estTableau = estTableau;
    }


    public String getTypestr() {
        return typeStr;
    }

    public void setTypestr(String typeStr) {
        this.typeStr = typeStr;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public boolean getEsttableau() {
        return estTableau;
    }

    public void setEsttableau(boolean estTableau) {
        this.estTableau = estTableau;
    }

    public Data_Classe getData_classe() {
        return data_classe;
    }

    public void setData_classe(Data_Classe data_classe) {
        this.data_classe = data_classe;
    }
    public Data_Classe getData_classe() {
        return data_classe;
    }

    public void setData_classe(Data_Classe data_classe) {
        this.data_classe = data_classe;
    }

}