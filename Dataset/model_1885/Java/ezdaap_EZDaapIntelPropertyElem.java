





import java.util.List;
import java.util.ArrayList;

public class ezdaap_EZDaapIntelPropertyElem  {

    private String license;





    private List<ezdaap_EZDaapArtist> ezdaap_ezdaapartists;


    public ezdaap_EZDaapIntelPropertyElem(
        String license    ) {
        this.license = license;
        this.ezdaap_ezdaapartists = new ArrayList<>();
    }

    public ezdaap_EZDaapIntelPropertyElem(
        String license        ArrayList<ezdaap_EZDaapArtist> ezdaap_ezdaapartists    ) {
        this.license = license;
        this.ezdaap_ezdaapartists = ezdaap_ezdaapartists;
    }

    public String getLicense() {
        return license;
    }

    public void setLicense(String license) {
        this.license = license;
    }

    public List<ezdaap_EZDaapArtist> getEzdaap_ezdaapartists() {
        return ezdaap_ezdaapartists;
    }

    public void addEzdaap_ezdaapartist(Ezdaap_ezdaapartist ezdaap_ezdaapartist) {
        this.ezdaap_ezdaapartists.add(ezdaap_ezdaapartist);
    }

}