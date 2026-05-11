





import java.util.List;
import java.util.ArrayList;

public class r2_PIVLTS extends QTY {

    private String alignment;
    private String isFlexible;





    private r2_PQ r2_pq;




    private r2_INT r2_int;




    private r2_RTO r2_rto;


    public r2_PIVLTS(
        String alignment,        String isFlexible    ) {
        super(
        );
        this.alignment = alignment;
        this.isFlexible = isFlexible;
    }


    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }
    public String getIsflexible() {
        return isFlexible;
    }

    public void setIsflexible(String isFlexible) {
        this.isFlexible = isFlexible;
    }

    public r2_PQ getR2_pq() {
        return r2_pq;
    }

    public void setR2_pq(r2_PQ r2_pq) {
        this.r2_pq = r2_pq;
    }
    public r2_INT getR2_int() {
        return r2_int;
    }

    public void setR2_int(r2_INT r2_int) {
        this.r2_int = r2_int;
    }
    public r2_RTO getR2_rto() {
        return r2_rto;
    }

    public void setR2_rto(r2_RTO r2_rto) {
        this.r2_rto = r2_rto;
    }

}