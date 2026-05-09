





import java.util.List;
import java.util.ArrayList;

public class ast_Modifier extends ASTNode, IExtendedModifier {

    private String keyword;



    public ast_Modifier(
        String keyword    ) {
        super(
        );
        this.keyword = keyword;
    }


    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }


}