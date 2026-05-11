





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSStringConstant extends BSExpression {

    private String value;



    public blorqueScript_BSStringConstant(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}