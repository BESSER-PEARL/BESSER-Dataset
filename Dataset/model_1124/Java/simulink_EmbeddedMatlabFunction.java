





import java.util.List;
import java.util.ArrayList;

public class simulink_EmbeddedMatlabFunction extends Block {

    private String code;



    public simulink_EmbeddedMatlabFunction(
        String code    ) {
        super(
        );
        this.code = code;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}