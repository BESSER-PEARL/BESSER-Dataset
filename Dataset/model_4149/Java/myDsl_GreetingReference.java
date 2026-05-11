





import java.util.List;
import java.util.ArrayList;

public class myDsl_GreetingReference extends AbstractGreeting {






    private myDsl_AbstractGreeting mydsl_abstractgreeting;


    public myDsl_GreetingReference(
    ) {
        super(
        );
    }



    public myDsl_AbstractGreeting getMydsl_abstractgreeting() {
        return mydsl_abstractgreeting;
    }

    public void setMydsl_abstractgreeting(myDsl_AbstractGreeting mydsl_abstractgreeting) {
        this.mydsl_abstractgreeting = mydsl_abstractgreeting;
    }

}