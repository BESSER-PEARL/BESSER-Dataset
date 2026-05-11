





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSParameter extends BSSymbol {

    private boolean isArray;



    public blorqueScript_BSParameter(
        boolean isArray    ) {
        super(
        );
        this.isArray = isArray;
    }


    public boolean getIsarray() {
        return isArray;
    }

    public void setIsarray(boolean isArray) {
        this.isArray = isArray;
    }


}