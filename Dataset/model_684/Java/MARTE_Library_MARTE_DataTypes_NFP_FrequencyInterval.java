





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_MARTE_DataTypes_NFP_FrequencyInterval  {






    private List<NFP_Frequency> nfp_frequencys;


    public MARTE_Library_MARTE_DataTypes_NFP_FrequencyInterval(
    ) {
        this.nfp_frequencys = new ArrayList<>();
    }

    public MARTE_Library_MARTE_DataTypes_NFP_FrequencyInterval(
        ArrayList<NFP_Frequency> nfp_frequencys    ) {
        this.nfp_frequencys = nfp_frequencys;
    }


    public List<NFP_Frequency> getNfp_frequencys() {
        return nfp_frequencys;
    }

    public void addNfp_frequency(Nfp_frequency nfp_frequency) {
        this.nfp_frequencys.add(nfp_frequency);
    }

}