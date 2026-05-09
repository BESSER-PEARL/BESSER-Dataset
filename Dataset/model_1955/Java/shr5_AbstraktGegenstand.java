





import java.util.List;
import java.util.ArrayList;

public class shr5_AbstraktGegenstand extends Anwendbar, Modifizierbar, Quelle, GeldWert, Beschreibbar {






    private shr5_MatrixDevice shr5_matrixdevice;


    public shr5_AbstraktGegenstand(
    ) {
        super(
        );
    }



    public shr5_MatrixDevice getShr5_matrixdevice() {
        return shr5_matrixdevice;
    }

    public void setShr5_matrixdevice(shr5_MatrixDevice shr5_matrixdevice) {
        this.shr5_matrixdevice = shr5_matrixdevice;
    }

}