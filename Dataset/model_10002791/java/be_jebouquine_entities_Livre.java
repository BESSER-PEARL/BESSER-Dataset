




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Livre  {

    private String photoLivre;
    private int idLangue;
    private int idCategorie;
    private String isbn;
    private LocalDate dateApparition;
    private int idLivre;
    private String titre;
    private int quantiteEnStock;
    private int idEditeur;
    private int idAuteur;
    private float prix;





    private List<be_jebouquine_entities_Commentaire> be_jebouquine_entities_commentaires;




    private be_jebouquine_entities_Langue be_jebouquine_entities_langue;




    private List<be_jebouquine_entities_LigneCommande> be_jebouquine_entities_lignecommandes;


    public be_jebouquine_entities_Livre(
        String photoLivre,        int idLangue,        int idCategorie,        String isbn,        LocalDate dateApparition,        int idLivre,        String titre,        int quantiteEnStock,        int idEditeur,        int idAuteur,        float prix    ) {
        this.photoLivre = photoLivre;
        this.idLangue = idLangue;
        this.idCategorie = idCategorie;
        this.isbn = isbn;
        this.dateApparition = dateApparition;
        this.idLivre = idLivre;
        this.titre = titre;
        this.quantiteEnStock = quantiteEnStock;
        this.idEditeur = idEditeur;
        this.idAuteur = idAuteur;
        this.prix = prix;
        this.be_jebouquine_entities_commentaires = new ArrayList<>();
        this.be_jebouquine_entities_lignecommandes = new ArrayList<>();
    }

    public be_jebouquine_entities_Livre(
        String photoLivre,        int idLangue,        int idCategorie,        String isbn,        LocalDate dateApparition,        int idLivre,        String titre,        int quantiteEnStock,        int idEditeur,        int idAuteur,        float prix        ArrayList<be_jebouquine_entities_Commentaire> be_jebouquine_entities_commentaires,        ArrayList<be_jebouquine_entities_LigneCommande> be_jebouquine_entities_lignecommandes    ) {
        this.photoLivre = photoLivre;
        this.idLangue = idLangue;
        this.idCategorie = idCategorie;
        this.isbn = isbn;
        this.dateApparition = dateApparition;
        this.idLivre = idLivre;
        this.titre = titre;
        this.quantiteEnStock = quantiteEnStock;
        this.idEditeur = idEditeur;
        this.idAuteur = idAuteur;
        this.prix = prix;
        this.be_jebouquine_entities_commentaires = be_jebouquine_entities_commentaires;
        this.be_jebouquine_entities_lignecommandes = be_jebouquine_entities_lignecommandes;
    }

    public String getPhotolivre() {
        return photoLivre;
    }

    public void setPhotolivre(String photoLivre) {
        this.photoLivre = photoLivre;
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
    public int getIdlivre() {
        return idLivre;
    }

    public void setIdlivre(int idLivre) {
        this.idLivre = idLivre;
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
    public int getIdediteur() {
        return idEditeur;
    }

    public void setIdediteur(int idEditeur) {
        this.idEditeur = idEditeur;
    }
    public int getIdauteur() {
        return idAuteur;
    }

    public void setIdauteur(int idAuteur) {
        this.idAuteur = idAuteur;
    }
    public float getPrix() {
        return prix;
    }

    public void setPrix(float prix) {
        this.prix = prix;
    }

    public List<be_jebouquine_entities_Commentaire> getBe_jebouquine_entities_commentaires() {
        return be_jebouquine_entities_commentaires;
    }

    public void addBe_jebouquine_entities_commentaire(Be_jebouquine_entities_commentaire be_jebouquine_entities_commentaire) {
        this.be_jebouquine_entities_commentaires.add(be_jebouquine_entities_commentaire);
    }
    public be_jebouquine_entities_Langue getBe_jebouquine_entities_langue() {
        return be_jebouquine_entities_langue;
    }

    public void setBe_jebouquine_entities_langue(be_jebouquine_entities_Langue be_jebouquine_entities_langue) {
        this.be_jebouquine_entities_langue = be_jebouquine_entities_langue;
    }
    public List<be_jebouquine_entities_LigneCommande> getBe_jebouquine_entities_lignecommandes() {
        return be_jebouquine_entities_lignecommandes;
    }

    public void addBe_jebouquine_entities_lignecommande(Be_jebouquine_entities_lignecommande be_jebouquine_entities_lignecommande) {
        this.be_jebouquine_entities_lignecommandes.add(be_jebouquine_entities_lignecommande);
    }

}