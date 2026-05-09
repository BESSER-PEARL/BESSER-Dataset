





import java.util.List;
import java.util.ArrayList;

public class oaam_library_WireType extends OaamBaseElementA {

    private float specificWeight;
    private float mtbf;
    private float specificPrice;
    private int nConductors;
    private int nShields;
    private float minBendingRadius;



    public oaam_library_WireType(
        float specificWeight,        float mtbf,        float specificPrice,        int nConductors,        int nShields,        float minBendingRadius    ) {
        super(
        );
        this.specificWeight = specificWeight;
        this.mtbf = mtbf;
        this.specificPrice = specificPrice;
        this.nConductors = nConductors;
        this.nShields = nShields;
        this.minBendingRadius = minBendingRadius;
    }


    public float getSpecificweight() {
        return specificWeight;
    }

    public void setSpecificweight(float specificWeight) {
        this.specificWeight = specificWeight;
    }
    public float getMtbf() {
        return mtbf;
    }

    public void setMtbf(float mtbf) {
        this.mtbf = mtbf;
    }
    public float getSpecificprice() {
        return specificPrice;
    }

    public void setSpecificprice(float specificPrice) {
        this.specificPrice = specificPrice;
    }
    public int getNconductors() {
        return nConductors;
    }

    public void setNconductors(int nConductors) {
        this.nConductors = nConductors;
    }
    public int getNshields() {
        return nShields;
    }

    public void setNshields(int nShields) {
        this.nShields = nShields;
    }
    public float getMinbendingradius() {
        return minBendingRadius;
    }

    public void setMinbendingradius(float minBendingRadius) {
        this.minBendingRadius = minBendingRadius;
    }


}