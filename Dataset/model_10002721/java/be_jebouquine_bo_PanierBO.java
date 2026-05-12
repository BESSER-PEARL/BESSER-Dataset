




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_bo_PanierBO  {

    private None listLivres;
    private int idPanier;
    private int quantity;
    private LocalDate date;



    public be_jebouquine_bo_PanierBO(
        None listLivres,        int idPanier,        int quantity,        LocalDate date    ) {
        this.listLivres = listLivres;
        this.idPanier = idPanier;
        this.quantity = quantity;
        this.date = date;
    }


    public None getListlivres() {
        return listLivres;
    }

    public void setListlivres(None listLivres) {
        this.listLivres = listLivres;
    }
    public int getIdpanier() {
        return idPanier;
    }

    public void setIdpanier(int idPanier) {
        this.idPanier = idPanier;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}