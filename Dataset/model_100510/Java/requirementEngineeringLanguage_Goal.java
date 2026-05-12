





import java.util.List;
import java.util.ArrayList;

public class requirementEngineeringLanguage_Goal extends Then {

    private String function;
    private String data;



    public requirementEngineeringLanguage_Goal(
        String function,        String data    ) {
        super(
        );
        this.function = function;
        this.data = data;
    }


    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }


}