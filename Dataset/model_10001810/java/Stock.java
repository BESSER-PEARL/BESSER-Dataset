





import java.util.List;
import java.util.ArrayList;

public class Stock  {

    private boolean disponibilit_;
    private int ingredient_id;
    private int quantit_;
    private int date_modification;



    public Stock(
        boolean disponibilit_,        int ingredient_id,        int quantit_,        int date_modification    ) {
        this.disponibilit_ = disponibilit_;
        this.ingredient_id = ingredient_id;
        this.quantit_ = quantit_;
        this.date_modification = date_modification;
    }


    public boolean getDisponibilit_() {
        return disponibilit_;
    }

    public void setDisponibilit_(boolean disponibilit_) {
        this.disponibilit_ = disponibilit_;
    }
    public int getIngredient_id() {
        return ingredient_id;
    }

    public void setIngredient_id(int ingredient_id) {
        this.ingredient_id = ingredient_id;
    }
    public int getQuantit_() {
        return quantit_;
    }

    public void setQuantit_(int quantit_) {
        this.quantit_ = quantit_;
    }
    public int getDate_modification() {
        return date_modification;
    }

    public void setDate_modification(int date_modification) {
        this.date_modification = date_modification;
    }


}