





import java.util.List;
import java.util.ArrayList;

public class nuSMV_CtlSpecification extends ModuleElement {

    private String name;
    private boolean nameKeyWord;
    private String specKeyWord;
    private boolean semicolon;



    public nuSMV_CtlSpecification(
        String name,        boolean nameKeyWord,        String specKeyWord,        boolean semicolon    ) {
        super(
        );
        this.name = name;
        this.nameKeyWord = nameKeyWord;
        this.specKeyWord = specKeyWord;
        this.semicolon = semicolon;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getNamekeyword() {
        return nameKeyWord;
    }

    public void setNamekeyword(boolean nameKeyWord) {
        this.nameKeyWord = nameKeyWord;
    }
    public String getSpeckeyword() {
        return specKeyWord;
    }

    public void setSpeckeyword(String specKeyWord) {
        this.specKeyWord = specKeyWord;
    }
    public boolean getSemicolon() {
        return semicolon;
    }

    public void setSemicolon(boolean semicolon) {
        this.semicolon = semicolon;
    }


}