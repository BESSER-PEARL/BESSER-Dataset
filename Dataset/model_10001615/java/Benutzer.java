





import java.util.List;
import java.util.ArrayList;

public class Benutzer  {

    private String Nachname;
    private String Vorname;
    private String Info;
    private String profilbild;





    private Registrieren registrieren;




    private Anmelden anmelden;




    private List<Hashtag> hashtags;




    private List<Freund> freunds;




    private List<Group> groups;




    private List<_unnamed> _unnameds;


    public Benutzer(
        String Nachname,        String Vorname,        String Info,        String profilbild    ) {
        this.Nachname = Nachname;
        this.Vorname = Vorname;
        this.Info = Info;
        this.profilbild = profilbild;
        this.hashtags = new ArrayList<>();
        this.freunds = new ArrayList<>();
        this.groups = new ArrayList<>();
        this._unnameds = new ArrayList<>();
    }

    public Benutzer(
        String Nachname,        String Vorname,        String Info,        String profilbild        ArrayList<Hashtag> hashtags,        ArrayList<Freund> freunds,        ArrayList<Group> groups,        ArrayList<_unnamed> _unnameds    ) {
        this.Nachname = Nachname;
        this.Vorname = Vorname;
        this.Info = Info;
        this.profilbild = profilbild;
        this.hashtags = hashtags;
        this.freunds = freunds;
        this.groups = groups;
        this._unnameds = _unnameds;
    }

    public String getNachname() {
        return Nachname;
    }

    public void setNachname(String Nachname) {
        this.Nachname = Nachname;
    }
    public String getVorname() {
        return Vorname;
    }

    public void setVorname(String Vorname) {
        this.Vorname = Vorname;
    }
    public String getInfo() {
        return Info;
    }

    public void setInfo(String Info) {
        this.Info = Info;
    }
    public String getProfilbild() {
        return profilbild;
    }

    public void setProfilbild(String profilbild) {
        this.profilbild = profilbild;
    }

    public Registrieren getRegistrieren() {
        return registrieren;
    }

    public void setRegistrieren(Registrieren registrieren) {
        this.registrieren = registrieren;
    }
    public Anmelden getAnmelden() {
        return anmelden;
    }

    public void setAnmelden(Anmelden anmelden) {
        this.anmelden = anmelden;
    }
    public List<Hashtag> getHashtags() {
        return hashtags;
    }

    public void addHashtag(Hashtag hashtag) {
        this.hashtags.add(hashtag);
    }
    public List<Freund> getFreunds() {
        return freunds;
    }

    public void addFreund(Freund freund) {
        this.freunds.add(freund);
    }
    public List<Group> getGroups() {
        return groups;
    }

    public void addGroup(Group group) {
        this.groups.add(group);
    }
    public List<_unnamed> get_unnameds() {
        return _unnameds;
    }

    public void add_unnamed(_unnamed _unnamed) {
        this._unnameds.add(_unnamed);
    }

}