





import java.util.List;
import java.util.ArrayList;

public class oclstdlibcs_PrecedenceCS extends NamedElementCS {

    private boolean isRightAssociative;



    public oclstdlibcs_PrecedenceCS(
        boolean isRightAssociative    ) {
        super(
        );
        this.isRightAssociative = isRightAssociative;
    }


    public boolean getIsrightassociative() {
        return isRightAssociative;
    }

    public void setIsrightassociative(boolean isRightAssociative) {
        this.isRightAssociative = isRightAssociative;
    }


}