




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_bo_PanierBO  {

    private int quantity;
    private LocalDate date;
    private int idPanier;
    private None listLivres;



    public be_jebouquine_bo_PanierBO(
        int quantity,        LocalDate date,        int idPanier,        None listLivres    ) {
        this.quantity = quantity;
        this.date = date;
        this.idPanier = idPanier;
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


}