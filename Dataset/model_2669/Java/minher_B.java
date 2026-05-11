





import java.util.List;
import java.util.ArrayList;

public class minher_B extends Named {

    private String value;





    private minher_A minher_a;


    public minher_B(
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

    public minher_A getMinher_a() {
        return minher_a;
    }

    public void setMinher_a(minher_A minher_a) {
        this.minher_a = minher_a;
    }

}