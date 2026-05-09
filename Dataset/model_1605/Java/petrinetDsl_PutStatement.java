





import java.util.List;
import java.util.ArrayList;

public class petrinetDsl_PutStatement  {

    private int count;





    private petrinetDsl_Resource petrinetdsl_resource;




    private petrinetDsl_Place petrinetdsl_place;




    private petrinetDsl_Transaction petrinetdsl_transaction;


    public petrinetDsl_PutStatement(
        int count    ) {
        this.count = count;
    }


    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public petrinetDsl_Resource getPetrinetdsl_resource() {
        return petrinetdsl_resource;
    }

    public void setPetrinetdsl_resource(petrinetDsl_Resource petrinetdsl_resource) {
        this.petrinetdsl_resource = petrinetdsl_resource;
    }
    public petrinetDsl_Place getPetrinetdsl_place() {
        return petrinetdsl_place;
    }

    public void setPetrinetdsl_place(petrinetDsl_Place petrinetdsl_place) {
        this.petrinetdsl_place = petrinetdsl_place;
    }
    public petrinetDsl_Transaction getPetrinetdsl_transaction() {
        return petrinetdsl_transaction;
    }

    public void setPetrinetdsl_transaction(petrinetDsl_Transaction petrinetdsl_transaction) {
        this.petrinetdsl_transaction = petrinetdsl_transaction;
    }

}