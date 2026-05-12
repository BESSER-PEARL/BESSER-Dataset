




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_bo_PanierBO  {

    private None listLivres;
    private int quantity;
    private int idPanier;
    private LocalDate date;



    public be_jebouquine_bo_PanierBO(
        None listLivres,        int quantity,        int idPanier,        LocalDate date    ) {
        this.listLivres = listLivres;
        this.quantity = quantity;
        this.idPanier = idPanier;
        this.date = date;
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
    public int getIdpanier() {
        return idPanier;
    }

    public void setIdpanier(int idPanier) {
        this.idPanier = idPanier;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}