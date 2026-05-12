




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Livre  {

    private int idLivre;
    private int idCategorie;
    private String titre;
    private int idEditeur;
    private String isbn;
    private LocalDate dateApparition;
    private int idLangue;
    private float prix;
    private String photoLivre;
    private int quantiteEnStock;
    private int idAuteur;



    public be_jebouquine_entities_Livre(
        int idLivre,        int idCategorie,        String titre,        int idEditeur,        String isbn,        LocalDate dateApparition,        int idLangue,        float prix,        String photoLivre,        int quantiteEnStock,        int idAuteur    ) {
        this.idLivre = idLivre;
        this.idCategorie = idCategorie;
        this.titre = titre;
        this.idEditeur = idEditeur;
        this.isbn = isbn;
        this.dateApparition = dateApparition;
        this.idLangue = idLangue;
        this.prix = prix;
        this.photoLivre = photoLivre;
        this.quantiteEnStock = quantiteEnStock;
        this.idAuteur = idAuteur;
    }


    public int getIdlivre() {
        return idLivre;
    }

    public void setIdlivre(int idLivre) {
        this.idLivre = idLivre;
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
    public LocalDate getDateapparition() {
        return dateApparition;
    }

    public void setDateapparition(LocalDate dateApparition) {
        this.dateApparition = dateApparition;
    }
    public int getIdlangue() {
        return idLangue;
    }

    public void setIdlangue(int idLangue) {
        this.idLangue = idLangue;
    }
    public float getPrix() {
        return prix;
    }

    public void setPrix(float prix) {
        this.prix = prix;
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
    public int getIdauteur() {
        return idAuteur;
    }

    public void setIdauteur(int idAuteur) {
        this.idAuteur = idAuteur;
    }


}