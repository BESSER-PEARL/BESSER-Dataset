




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Livre  {

    private int idEditeur;
    private String isbn;
    private String titre;
    private int idCategorie;
    private int idAuteur;
    private int idLivre;
    private int quantiteEnStock;
    private LocalDate dateApparition;
    private String photoLivre;
    private float prix;
    private int idLangue;



    public be_jebouquine_entities_Livre(
        int idEditeur,        String isbn,        String titre,        int idCategorie,        int idAuteur,        int idLivre,        int quantiteEnStock,        LocalDate dateApparition,        String photoLivre,        float prix,        int idLangue    ) {
        this.idEditeur = idEditeur;
        this.isbn = isbn;
        this.titre = titre;
        this.idCategorie = idCategorie;
        this.idAuteur = idAuteur;
        this.idLivre = idLivre;
        this.quantiteEnStock = quantiteEnStock;
        this.dateApparition = dateApparition;
        this.photoLivre = photoLivre;
        this.prix = prix;
        this.idLangue = idLangue;
    }


    public int getIdediteur() {
        return idEditeur;
    }

    public void setIdediteur(int idEditeur) {
        this.idEditeur = idEditeur;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public String getTitre() {
        return titre;
    }

    public void setTitre(String titre) {
        this.titre = titre;
    }
    public int getIdcategorie() {
        return idCategorie;
    }

    public void setIdcategorie(int idCategorie) {
        this.idCategorie = idCategorie;
    }
    public int getIdauteur() {
        return idAuteur;
    }

    public void setIdauteur(int idAuteur) {
        this.idAuteur = idAuteur;
    }
    public int getIdlivre() {
        return idLivre;
    }

    public void setIdlivre(int idLivre) {
        this.idLivre = idLivre;
    }
    public int getQuantiteenstock() {
        return quantiteEnStock;
    }

    public void setQuantiteenstock(int quantiteEnStock) {
        this.quantiteEnStock = quantiteEnStock;
    }
    public LocalDate getDateapparition() {
        return dateApparition;
    }

    public void setDateapparition(LocalDate dateApparition) {
        this.dateApparition = dateApparition;
    }
    public String getPhotolivre() {
        return photoLivre;
    }

    public void setPhotolivre(String photoLivre) {
        this.photoLivre = photoLivre;
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


}