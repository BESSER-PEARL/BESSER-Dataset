




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Livre  {

    private int idCategorie;
    private String titre;
    private int quantiteEnStock;
    private float prix;
    private String photoLivre;
    private LocalDate dateApparition;
    private int idAuteur;
    private int idLangue;
    private int idLivre;
    private String isbn;
    private int idEditeur;



    public be_jebouquine_entities_Livre(
        int idCategorie,        String titre,        int quantiteEnStock,        float prix,        String photoLivre,        LocalDate dateApparition,        int idAuteur,        int idLangue,        int idLivre,        String isbn,        int idEditeur    ) {
        this.idCategorie = idCategorie;
        this.titre = titre;
        this.quantiteEnStock = quantiteEnStock;
        this.prix = prix;
        this.photoLivre = photoLivre;
        this.dateApparition = dateApparition;
        this.idAuteur = idAuteur;
        this.idLangue = idLangue;
        this.idLivre = idLivre;
        this.isbn = isbn;
        this.idEditeur = idEditeur;
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
    public int getQuantiteenstock() {
        return quantiteEnStock;
    }

    public void setQuantiteenstock(int quantiteEnStock) {
        this.quantiteEnStock = quantiteEnStock;
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
    public int getIdlangue() {
        return idLangue;
    }

    public void setIdlangue(int idLangue) {
        this.idLangue = idLangue;
    }
    public int getIdlivre() {
        return idLivre;
    }

    public void setIdlivre(int idLivre) {
        this.idLivre = idLivre;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public int getIdediteur() {
        return idEditeur;
    }

    public void setIdediteur(int idEditeur) {
        this.idEditeur = idEditeur;
    }


}