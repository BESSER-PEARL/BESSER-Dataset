





import java.util.List;
import java.util.ArrayList;

public class JMM_Model  {

    private String name;



    public JMM_Model(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}