





import java.util.List;
import java.util.ArrayList;

public class model_ReceptionistController extends BookingController, ReceptionistInterface {






    private model_UserExpert model_userexpert;


    public model_ReceptionistController(
    ) {
        super(
        );
    }



    public model_UserExpert getModel_userexpert() {
        return model_userexpert;
    }

    public void setModel_userexpert(model_UserExpert model_userexpert) {
        this.model_userexpert = model_userexpert;
    }

}