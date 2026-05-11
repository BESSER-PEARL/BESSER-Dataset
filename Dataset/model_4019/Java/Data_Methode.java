





import java.util.List;
import java.util.ArrayList;

public class Data_Methode  {

    private String typeRetour;
    private String nom;





    private List<Data_Attribut> data_attributs;




    private Data_Classe data_classe;


    public Data_Methode(
        String typeRetour,        String nom    ) {
        this.typeRetour = typeRetour;
        this.nom = nom;
        this.data_attributs = new ArrayList<>();
    }

    public Data_Methode(
        String typeRetour,        String nom        ArrayList<Data_Attribut> data_attributs    ) {
        this.typeRetour = typeRetour;
        this.nom = nom;
        this.data_attributs = data_attributs;
    }

    public String getTyperetour() {
        return typeRetour;
    }

    public void setTyperetour(String typeRetour) {
        this.typeRetour = typeRetour;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public List<Data_Attribut> getData_attributs() {
        return data_attributs;
    }

    public void addData_attribut(Data_attribut data_attribut) {
        this.data_attributs.add(data_attribut);
    }
    public Data_Classe getData_classe() {
        return data_classe;
    }

    public void setData_classe(Data_Classe data_classe) {
        this.data_classe = data_classe;
    }

}