




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_bo_PanierBO  {

    private int idPanier;
    private None listLivres;
    private int quantity;
    private LocalDate date;



    public be_jebouquine_bo_PanierBO(
        int idPanier,        None listLivres,        int quantity,        LocalDate date    ) {
        this.idPanier = idPanier;
        this.listLivres = listLivres;
        this.quantity = quantity;
        this.date = date;
    }


    public int getIdpanier() {
        return idPanier;
    }

    public void setIdpanier(int idPanier) {
        this.idPanier = idPanier;
    }
    public None getListlivres() {
        return listLivres;
    }

    public void setListlivres(None listLivres) {
        this.listLivres = listLivres;
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