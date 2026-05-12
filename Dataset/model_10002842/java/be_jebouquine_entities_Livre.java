




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Livre  {

    private int quantiteEnStock;
    private float prix;
    private LocalDate dateApparition;
    private int idAuteur;
    private int idLivre;
    private String photoLivre;
    private String isbn;
    private String titre;
    private int idLangue;
    private int idCategorie;
    private int idEditeur;



    public be_jebouquine_entities_Livre(
        int quantiteEnStock,        float prix,        LocalDate dateApparition,        int idAuteur,        int idLivre,        String photoLivre,        String isbn,        String titre,        int idLangue,        int idCategorie,        int idEditeur    ) {
        this.quantiteEnStock = quantiteEnStock;
        this.prix = prix;
        this.dateApparition = dateApparition;
        this.idAuteur = idAuteur;
        this.idLivre = idLivre;
        this.photoLivre = photoLivre;
        this.isbn = isbn;
        this.titre = titre;
        this.idLangue = idLangue;
        this.idCategorie = idCategorie;
        this.idEditeur = idEditeur;
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
    public int getIdlivre() {
        return idLivre;
    }

    public void setIdlivre(int idLivre) {
        this.idLivre = idLivre;
    }
    public String getPhotolivre() {
        return photoLivre;
    }

    public void setPhotolivre(String photoLivre) {
        this.photoLivre = photoLivre;
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
    public int getIdlangue() {
        return idLangue;
    }

    public void setIdlangue(int idLangue) {
        this.idLangue = idLangue;
    }
    public int getIdcategorie() {
        return idCategorie;
    }

    public void setIdcategorie(int idCategorie) {
        this.idCategorie = idCategorie;
    }
    public int getIdediteur() {
        return idEditeur;
    }

    public void setIdediteur(int idEditeur) {
        this.idEditeur = idEditeur;
    }


}