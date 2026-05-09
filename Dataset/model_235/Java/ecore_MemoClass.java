





import java.util.List;
import java.util.ArrayList;

public class ecore_MemoClass extends EClass {

    private String instance;



    public ecore_MemoClass(
        String instance    ) {
        super(
        );
        this.instance = instance;
    }


    public String getInstance() {
        return instance;
    }

    public void setInstance(String instance) {
        this.instance = instance;
    }


}