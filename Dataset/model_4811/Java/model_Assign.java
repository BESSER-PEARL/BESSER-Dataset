





import java.util.List;
import java.util.ArrayList;

public class model_Assign extends Activity {

    private String validate;





    private List<model_Copy> model_copys;


    public model_Assign(
        String validate    ) {
        super(
        );
        this.validate = validate;
        this.model_copys = new ArrayList<>();
    }

    public model_Assign(
        String validate        ArrayList<model_Copy> model_copys    ) {
        this.validate = validate;
        this.model_copys = model_copys;
    }

    public String getValidate() {
        return validate;
    }

    public void setValidate(String validate) {
        this.validate = validate;
    }

    public List<model_Copy> getModel_copys() {
        return model_copys;
    }

    public void addModel_copy(Model_copy model_copy) {
        this.model_copys.add(model_copy);
    }

}