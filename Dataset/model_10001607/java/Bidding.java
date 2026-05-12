





import java.util.List;
import java.util.ArrayList;

public class Bidding  {

    private String bidder;
    private String jabatan;
    private String berkas;
    private String catatanBidder;
    private String notulensi;
    private String biddee;
    private int nilai;
    private String statusBidding;





    private List<Bidder> bidders;




    private Admin admin;




    private List<Bidder> bidders;




    private List<Biddee> biddees;


    public Bidding(
        String bidder,        String jabatan,        String berkas,        String catatanBidder,        String notulensi,        String biddee,        int nilai,        String statusBidding    ) {
        this.bidder = bidder;
        this.jabatan = jabatan;
        this.berkas = berkas;
        this.catatanBidder = catatanBidder;
        this.notulensi = notulensi;
        this.biddee = biddee;
        this.nilai = nilai;
        this.statusBidding = statusBidding;
        this.bidders = new ArrayList<>();
        this.bidders = new ArrayList<>();
        this.biddees = new ArrayList<>();
    }

    public Bidding(
        String bidder,        String jabatan,        String berkas,        String catatanBidder,        String notulensi,        String biddee,        int nilai,        String statusBidding        ArrayList<Bidder> bidders,        ArrayList<Bidder> bidders,        ArrayList<Biddee> biddees    ) {
        this.bidder = bidder;
        this.jabatan = jabatan;
        this.berkas = berkas;
        this.catatanBidder = catatanBidder;
        this.notulensi = notulensi;
        this.biddee = biddee;
        this.nilai = nilai;
        this.statusBidding = statusBidding;
        this.bidders = bidders;
        this.bidders = bidders;
        this.biddees = biddees;
    }

    public String getBidder() {
        return bidder;
    }

    public void setBidder(String bidder) {
        this.bidder = bidder;
    }
    public String getJabatan() {
        return jabatan;
    }

    public void setJabatan(String jabatan) {
        this.jabatan = jabatan;
    }
    public String getBerkas() {
        return berkas;
    }

    public void setBerkas(String berkas) {
        this.berkas = berkas;
    }
    public String getCatatanbidder() {
        return catatanBidder;
    }

    public void setCatatanbidder(String catatanBidder) {
        this.catatanBidder = catatanBidder;
    }
    public String getNotulensi() {
        return notulensi;
    }

    public void setNotulensi(String notulensi) {
        this.notulensi = notulensi;
    }
    public String getBiddee() {
        return biddee;
    }

    public void setBiddee(String biddee) {
        this.biddee = biddee;
    }
    public int getNilai() {
        return nilai;
    }

    public void setNilai(int nilai) {
        this.nilai = nilai;
    }
    public String getStatusbidding() {
        return statusBidding;
    }

    public void setStatusbidding(String statusBidding) {
        this.statusBidding = statusBidding;
    }

    public List<Bidder> getBidders() {
        return bidders;
    }

    public void addBidder(Bidder bidder) {
        this.bidders.add(bidder);
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public List<Bidder> getBidders() {
        return bidders;
    }

    public void addBidder(Bidder bidder) {
        this.bidders.add(bidder);
    }
    public List<Biddee> getBiddees() {
        return biddees;
    }

    public void addBiddee(Biddee biddee) {
        this.biddees.add(biddee);
    }

}