





import java.util.List;
import java.util.ArrayList;

public class model_TableContentWithInnerChild extends TableContent {

    private String stuff;





    private model_TableContent model_tablecontent;


    public model_TableContentWithInnerChild(
        String stuff    ) {
        super(
        );
        this.stuff = stuff;
    }


    public String getStuff() {
        return stuff;
    }

    public void setStuff(String stuff) {
        this.stuff = stuff;
    }

    public model_TableContent getModel_tablecontent() {
        return model_tablecontent;
    }

    public void setModel_tablecontent(model_TableContent model_tablecontent) {
        this.model_tablecontent = model_tablecontent;
    }

}