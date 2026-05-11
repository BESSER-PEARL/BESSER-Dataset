





import java.util.List;
import java.util.ArrayList;

public class nuSMV_WordType extends SimpleType {

    private String wordNumber;



    public nuSMV_WordType(
        String wordNumber    ) {
        super(
        );
        this.wordNumber = wordNumber;
    }


    public String getWordnumber() {
        return wordNumber;
    }

    public void setWordnumber(String wordNumber) {
        this.wordNumber = wordNumber;
    }


}