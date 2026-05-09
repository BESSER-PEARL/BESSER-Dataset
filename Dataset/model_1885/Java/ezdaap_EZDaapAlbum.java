





import java.util.List;
import java.util.ArrayList;

public class ezdaap_EZDaapAlbum extends EZDaapIntelPropertyElem, EZDaapElem {






    private List<ezdaap_EZDaapSong> ezdaap_ezdaapsongs;


    public ezdaap_EZDaapAlbum(
    ) {
        super(
        );
        this.ezdaap_ezdaapsongs = new ArrayList<>();
    }

    public ezdaap_EZDaapAlbum(
        ArrayList<ezdaap_EZDaapSong> ezdaap_ezdaapsongs    ) {
        this.ezdaap_ezdaapsongs = ezdaap_ezdaapsongs;
    }


    public List<ezdaap_EZDaapSong> getEzdaap_ezdaapsongs() {
        return ezdaap_ezdaapsongs;
    }

    public void addEzdaap_ezdaapsong(Ezdaap_ezdaapsong ezdaap_ezdaapsong) {
        this.ezdaap_ezdaapsongs.add(ezdaap_ezdaapsong);
    }

}