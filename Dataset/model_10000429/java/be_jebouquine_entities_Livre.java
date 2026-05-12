




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Livre  {

    private int quantiteEnStock;
    private int idAuteur;
    private String photoLivre;
    private String titre;
    private float prix;
    private LocalDate dateApparition;
    private int idEditeur;
    private int idCategorie;
    private int idLangue;
    private String isbn;
    private int idLivre;



    public be_jebouquine_entities_Livre(
        int quantiteEnStock,        int idAuteur,        String photoLivre,        String titre,        float prix,        LocalDate dateApparition,        int idEditeur,        int idCategorie,        int idLangue,        String isbn,        int idLivre    ) {
        this.quantiteEnStock = quantiteEnStock;
        this.idAuteur = idAuteur;
        this.photoLivre = photoLivre;
        this.titre = titre;
        this.prix = prix;
        this.dateApparition = dateApparition;
        this.idEditeur = idEditeur;
        this.idCategorie = idCategorie;
        this.idLangue = idLangue;
        this.isbn = isbn;
        this.idLivre = idLivre;
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
    public String getTitre() {
        return titre;
    }

    public void setTitre(String titre) {
        this.titre = titre;
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
    public int getIdediteur() {
        return idEditeur;
    }

    public void setIdediteur(int idEditeur) {
        this.idEditeur = idEditeur;
    }
    public int getIdcategorie() {
        return idCategorie;
    }

    public void setIdcategorie(int idCategorie) {
        this.idCategorie = idCategorie;
    }
    public int getIdlangue() {
        return idLangue;
    }

    public void setIdlangue(int idLangue) {
        this.idLangue = idLangue;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public int getIdlivre() {
        return idLivre;
    }

    public void setIdlivre(int idLivre) {
        this.idLivre = idLivre;
    }


}