




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Livre  {

    private String titre;
    private int idLivre;
    private float prix;
    private LocalDate dateApparition;
    private int idAuteur;
    private int idEditeur;
    private String photoLivre;
    private int quantiteEnStock;
    private int idCategorie;
    private String isbn;
    private int idLangue;



    public be_jebouquine_entities_Livre(
        String titre,        int idLivre,        float prix,        LocalDate dateApparition,        int idAuteur,        int idEditeur,        String photoLivre,        int quantiteEnStock,        int idCategorie,        String isbn,        int idLangue    ) {
        this.titre = titre;
        this.idLivre = idLivre;
        this.prix = prix;
        this.dateApparition = dateApparition;
        this.idAuteur = idAuteur;
        this.idEditeur = idEditeur;
        this.photoLivre = photoLivre;
        this.quantiteEnStock = quantiteEnStock;
        this.idCategorie = idCategorie;
        this.isbn = isbn;
        this.idLangue = idLangue;
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
    public float getPrix() {
        return prix;
    }

    public void setPrix(float prix) {
        this.prix = prix;
    }
    public LocalDate getDateapparition() {
        return dateApparition;
    }

    public void setDateapparition(LocalDate dateApparition) {
        this.dateApparition = dateApparition;
    }
    public int getIdauteur() {
        return idAuteur;
    }

    public void setIdauteur(int idAuteur) {
        this.idAuteur = idAuteur;
    }
    public int getIdediteur() {
        return idEditeur;
    }

    public void setIdediteur(int idEditeur) {
        this.idEditeur = idEditeur;
    }
    public String getPhotolivre() {
        return photoLivre;
    }

    public void setPhotolivre(String photoLivre) {
        this.photoLivre = photoLivre;
    }
    public int getQuantiteenstock() {
        return quantiteEnStock;
    }

    public void setQuantiteenstock(int quantiteEnStock) {
        this.quantiteEnStock = quantiteEnStock;
    }
    public int getIdcategorie() {
        return idCategorie;
    }

    public void setIdcategorie(int idCategorie) {
        this.idCategorie = idCategorie;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public int getIdlangue() {
        return idLangue;
    }

    public void setIdlangue(int idLangue) {
        this.idLangue = idLangue;
    }


}