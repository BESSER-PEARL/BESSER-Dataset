





import java.util.List;
import java.util.ArrayList;

public class ezdaap_EZDaapITunesInstance  {

    private int sessionID;
    private String serverName;
    private String id;
    private int revID;





    private List<ezdaap_EZDaapArtist> ezdaap_ezdaapartists;




    private List<ezdaap_EZDaapAlbum> ezdaap_ezdaapalbums;




    private List<ezdaap_EZDaapPlayList> ezdaap_ezdaapplaylists;




    private List<ezdaap_EZDaapSong> ezdaap_ezdaapsongs;


    public ezdaap_EZDaapITunesInstance(
        int sessionID,        String serverName,        String id,        int revID    ) {
        this.sessionID = sessionID;
        this.serverName = serverName;
        this.id = id;
        this.revID = revID;
        this.ezdaap_ezdaapartists = new ArrayList<>();
        this.ezdaap_ezdaapalbums = new ArrayList<>();
        this.ezdaap_ezdaapplaylists = new ArrayList<>();
        this.ezdaap_ezdaapsongs = new ArrayList<>();
    }

    public ezdaap_EZDaapITunesInstance(
        int sessionID,        String serverName,        String id,        int revID        ArrayList<ezdaap_EZDaapArtist> ezdaap_ezdaapartists,        ArrayList<ezdaap_EZDaapAlbum> ezdaap_ezdaapalbums,        ArrayList<ezdaap_EZDaapPlayList> ezdaap_ezdaapplaylists,        ArrayList<ezdaap_EZDaapSong> ezdaap_ezdaapsongs    ) {
        this.sessionID = sessionID;
        this.serverName = serverName;
        this.id = id;
        this.revID = revID;
        this.ezdaap_ezdaapartists = ezdaap_ezdaapartists;
        this.ezdaap_ezdaapalbums = ezdaap_ezdaapalbums;
        this.ezdaap_ezdaapplaylists = ezdaap_ezdaapplaylists;
        this.ezdaap_ezdaapsongs = ezdaap_ezdaapsongs;
    }

    public int getSessionid() {
        return sessionID;
    }

    public void setSessionid(int sessionID) {
        this.sessionID = sessionID;
    }
    public String getServername() {
        return serverName;
    }

    public void setServername(String serverName) {
        this.serverName = serverName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getRevid() {
        return revID;
    }

    public void setRevid(int revID) {
        this.revID = revID;
    }

    public List<ezdaap_EZDaapArtist> getEzdaap_ezdaapartists() {
        return ezdaap_ezdaapartists;
    }

    public void addEzdaap_ezdaapartist(Ezdaap_ezdaapartist ezdaap_ezdaapartist) {
        this.ezdaap_ezdaapartists.add(ezdaap_ezdaapartist);
    }
    public List<ezdaap_EZDaapAlbum> getEzdaap_ezdaapalbums() {
        return ezdaap_ezdaapalbums;
    }

    public void addEzdaap_ezdaapalbum(Ezdaap_ezdaapalbum ezdaap_ezdaapalbum) {
        this.ezdaap_ezdaapalbums.add(ezdaap_ezdaapalbum);
    }
    public List<ezdaap_EZDaapPlayList> getEzdaap_ezdaapplaylists() {
        return ezdaap_ezdaapplaylists;
    }

    public void addEzdaap_ezdaapplaylist(Ezdaap_ezdaapplaylist ezdaap_ezdaapplaylist) {
        this.ezdaap_ezdaapplaylists.add(ezdaap_ezdaapplaylist);
    }
    public List<ezdaap_EZDaapSong> getEzdaap_ezdaapsongs() {
        return ezdaap_ezdaapsongs;
    }

    public void addEzdaap_ezdaapsong(Ezdaap_ezdaapsong ezdaap_ezdaapsong) {
        this.ezdaap_ezdaapsongs.add(ezdaap_ezdaapsong);
    }

}