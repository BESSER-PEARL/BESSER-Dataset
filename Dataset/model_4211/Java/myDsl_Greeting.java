





import java.util.List;
import java.util.ArrayList;

public class myDsl_Greeting extends Element {






    private myDsl_Person mydsl_person;


    public myDsl_Greeting(
    ) {
        super(
        );
    }



    public myDsl_Person getMydsl_person() {
        return mydsl_person;
    }

    public void setMydsl_person(myDsl_Person mydsl_person) {
        this.mydsl_person = mydsl_person;
    }

}