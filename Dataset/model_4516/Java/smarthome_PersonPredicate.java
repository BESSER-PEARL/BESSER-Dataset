





import java.util.List;
import java.util.ArrayList;

public class smarthome_PersonPredicate extends Predicate {

    private String activity;





    private smarthome_Person smarthome_person;


    public smarthome_PersonPredicate(
        String activity    ) {
        super(
        );
        this.activity = activity;
    }


    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }

    public smarthome_Person getSmarthome_person() {
        return smarthome_person;
    }

    public void setSmarthome_person(smarthome_Person smarthome_person) {
        this.smarthome_person = smarthome_person;
    }

}