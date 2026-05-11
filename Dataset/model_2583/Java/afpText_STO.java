





import java.util.List;
import java.util.ArrayList;

public class afpText_STO extends triplet {

    private String IORNTION;
    private String BORNTION;



    public afpText_STO(
        String IORNTION,        String BORNTION    ) {
        super(
        );
        this.IORNTION = IORNTION;
        this.BORNTION = BORNTION;
    }


    public String getIorntion() {
        return IORNTION;
    }

    public void setIorntion(String IORNTION) {
        this.IORNTION = IORNTION;
    }
    public String getBorntion() {
        return BORNTION;
    }

    public void setBorntion(String BORNTION) {
        this.BORNTION = BORNTION;
    }


}