





import java.util.List;
import java.util.ArrayList;

public class cobol_specialnames_CurrencySign extends specialnames_SpecialName, specialnames_SpecialNameStatement {

    private String pictureSymbol;





    private Literal literal;


    public cobol_specialnames_CurrencySign(
        String pictureSymbol    ) {
        super(
        );
        this.pictureSymbol = pictureSymbol;
    }


    public String getPicturesymbol() {
        return pictureSymbol;
    }

    public void setPicturesymbol(String pictureSymbol) {
        this.pictureSymbol = pictureSymbol;
    }

    public Literal getLiteral() {
        return literal;
    }

    public void setLiteral(Literal literal) {
        this.literal = literal;
    }

}