





import java.util.List;
import java.util.ArrayList;

public class ezdaap_EZDaapManager  {






    private List<ezdaap_EZDaapITunesInstance> ezdaap_ezdaapitunesinstances;


    public ezdaap_EZDaapManager(
    ) {
        this.ezdaap_ezdaapitunesinstances = new ArrayList<>();
    }

    public ezdaap_EZDaapManager(
        ArrayList<ezdaap_EZDaapITunesInstance> ezdaap_ezdaapitunesinstances    ) {
        this.ezdaap_ezdaapitunesinstances = ezdaap_ezdaapitunesinstances;
    }


    public List<ezdaap_EZDaapITunesInstance> getEzdaap_ezdaapitunesinstances() {
        return ezdaap_ezdaapitunesinstances;
    }

    public void addEzdaap_ezdaapitunesinstance(Ezdaap_ezdaapitunesinstance ezdaap_ezdaapitunesinstance) {
        this.ezdaap_ezdaapitunesinstances.add(ezdaap_ezdaapitunesinstance);
    }

}