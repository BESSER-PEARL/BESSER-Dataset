




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Livre  {

    private float prix;
    private int idLangue;
    private int quantiteEnStock;
    private int idAuteur;
    private String photoLivre;
    private int idCategorie;
    private String titre;
    private int idLivre;
    private int idEditeur;
    private LocalDate dateApparition;
    private String isbn;



    public be_jebouquine_entities_Livre(
        float prix,        int idLangue,        int quantiteEnStock,        int idAuteur,        String photoLivre,        int idCategorie,        String titre,        int idLivre,        int idEditeur,        LocalDate dateApparition,        String isbn    ) {
        this.prix = prix;
        this.idLangue = idLangue;
        this.quantiteEnStock = quantiteEnStock;
        this.idAuteur = idAuteur;
        this.photoLivre = photoLivre;
        this.idCategorie = idCategorie;
        this.titre = titre;
        this.idLivre = idLivre;
        this.idEditeur = idEditeur;
        this.dateApparition = dateApparition;
        this.isbn = isbn;
    }


    public float getPrix() {
        return prix;
    }

    public void setPrix(float prix) {
        this.prix = prix;
    }
    public int getIdlangue() {
        return idLangue;
    }

    public void setIdlangue(int idLangue) {
        this.idLangue = idLangue;
    }
    public int getQuantiteenstock() {
        return quantiteEnStock;
    }

    public void setQuantiteenstock(int quantiteEnStock) {
        this.quantiteEnStock = quantiteEnStock;
    }
    public int getIdauteur() {
        return idAuteur;
    }

    public void setIdauteur(int idAuteur) {
        this.idAuteur = idAuteur;
    }
    public String getPhotolivre() {
        return photoLivre;
    }

    public void setPhotolivre(String photoLivre) {
        this.photoLivre = photoLivre;
    }
    public int getIdcategorie() {
        return idCategorie;
    }

    public void setIdcategorie(int idCategorie) {
        this.idCategorie = idCategorie;
    }
    public String getTitre() {
        return titre;
    }

    public void setTitre(String titre) {
        this.titre = titre;
    }
    public int getIdlivre() {
        return idLivre;
    }

    public void setIdlivre(int idLivre) {
        this.idLivre = idLivre;
    }
    public int getIdediteur() {
        return idEditeur;
    }

    public void setIdediteur(int idEditeur) {
        this.idEditeur = idEditeur;
    }
    public LocalDate getDateapparition() {
        return dateApparition;
    }

    public void setDateapparition(LocalDate dateApparition) {
        this.dateApparition = dateApparition;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }


}