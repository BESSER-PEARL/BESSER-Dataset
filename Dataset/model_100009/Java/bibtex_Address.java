





import java.util.List;
import java.util.ArrayList;

public class bibtex_Address  {

    private String address;





    private bibtex_Book bibtex_book;




    private bibtex_Techreport bibtex_techreport;




    private bibtex_Phdthesis bibtex_phdthesis;




    private bibtex_Booklet bibtex_booklet;




    private bibtex_Incollection bibtex_incollection;




    private bibtex_Conference bibtex_conference;




    private bibtex_Mastersthesis bibtex_mastersthesis;




    private bibtex_Inbook bibtex_inbook;




    private bibtex_Proceedings bibtex_proceedings;




    private bibtex_Inproceedings bibtex_inproceedings;




    private bibtex_Manual bibtex_manual;


    public bibtex_Address(
        String address    ) {
        this.address = address;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public bibtex_Book getBibtex_book() {
        return bibtex_book;
    }

    public void setBibtex_book(bibtex_Book bibtex_book) {
        this.bibtex_book = bibtex_book;
    }
    public bibtex_Techreport getBibtex_techreport() {
        return bibtex_techreport;
    }

    public void setBibtex_techreport(bibtex_Techreport bibtex_techreport) {
        this.bibtex_techreport = bibtex_techreport;
    }
    public bibtex_Phdthesis getBibtex_phdthesis() {
        return bibtex_phdthesis;
    }

    public void setBibtex_phdthesis(bibtex_Phdthesis bibtex_phdthesis) {
        this.bibtex_phdthesis = bibtex_phdthesis;
    }
    public bibtex_Booklet getBibtex_booklet() {
        return bibtex_booklet;
    }

    public void setBibtex_booklet(bibtex_Booklet bibtex_booklet) {
        this.bibtex_booklet = bibtex_booklet;
    }
    public bibtex_Incollection getBibtex_incollection() {
        return bibtex_incollection;
    }

    public void setBibtex_incollection(bibtex_Incollection bibtex_incollection) {
        this.bibtex_incollection = bibtex_incollection;
    }
    public bibtex_Conference getBibtex_conference() {
        return bibtex_conference;
    }

    public void setBibtex_conference(bibtex_Conference bibtex_conference) {
        this.bibtex_conference = bibtex_conference;
    }
    public bibtex_Mastersthesis getBibtex_mastersthesis() {
        return bibtex_mastersthesis;
    }

    public void setBibtex_mastersthesis(bibtex_Mastersthesis bibtex_mastersthesis) {
        this.bibtex_mastersthesis = bibtex_mastersthesis;
    }
    public bibtex_Inbook getBibtex_inbook() {
        return bibtex_inbook;
    }

    public void setBibtex_inbook(bibtex_Inbook bibtex_inbook) {
        this.bibtex_inbook = bibtex_inbook;
    }
    public bibtex_Proceedings getBibtex_proceedings() {
        return bibtex_proceedings;
    }

    public void setBibtex_proceedings(bibtex_Proceedings bibtex_proceedings) {
        this.bibtex_proceedings = bibtex_proceedings;
    }
    public bibtex_Inproceedings getBibtex_inproceedings() {
        return bibtex_inproceedings;
    }

    public void setBibtex_inproceedings(bibtex_Inproceedings bibtex_inproceedings) {
        this.bibtex_inproceedings = bibtex_inproceedings;
    }
    public bibtex_Manual getBibtex_manual() {
        return bibtex_manual;
    }

    public void setBibtex_manual(bibtex_Manual bibtex_manual) {
        this.bibtex_manual = bibtex_manual;
    }

}