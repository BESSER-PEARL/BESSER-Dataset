





import java.util.List;
import java.util.ArrayList;

public class Produit  {

    private int id;
    private int categorie_id;
    private String prix;
    private String nom;





    private Cat_gorie cat_gorie;




    private Recette recette;


    public Produit(
        int id,        int categorie_id,        String prix,        String nom    ) {
        this.id = id;
        this.categorie_id = categorie_id;
        this.prix = prix;
        this.nom = nom;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getCategorie_id() {
        return categorie_id;
    }

    public void setCategorie_id(int categorie_id) {
        this.categorie_id = categorie_id;
    }
    public String getPrix() {
        return prix;
    }

    public void setPrix(String prix) {
        this.prix = prix;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public Cat_gorie getCat_gorie() {
        return cat_gorie;
    }

    public void setCat_gorie(Cat_gorie cat_gorie) {
        this.cat_gorie = cat_gorie;
    }
    public Recette getRecette() {
        return recette;
    }

    public void setRecette(Recette recette) {
        this.recette = recette;
    }

}