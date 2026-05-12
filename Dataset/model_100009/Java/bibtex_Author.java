





import java.util.List;
import java.util.ArrayList;

public class bibtex_Author  {

    private String author;





    private bibtex_Phdthesis bibtex_phdthesis;




    private bibtex_Article bibtex_article;




    private bibtex_Book bibtex_book;




    private bibtex_Misc bibtex_misc;




    private bibtex_Techreport bibtex_techreport;




    private bibtex_Manual bibtex_manual;




    private bibtex_Conference bibtex_conference;




    private bibtex_Inproceedings bibtex_inproceedings;




    private bibtex_Booklet bibtex_booklet;




    private bibtex_Incollection bibtex_incollection;




    private bibtex_Mastersthesis bibtex_mastersthesis;




    private bibtex_Unpublished bibtex_unpublished;


    public bibtex_Author(
        String author    ) {
        this.author = author;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public bibtex_Phdthesis getBibtex_phdthesis() {
        return bibtex_phdthesis;
    }

    public void setBibtex_phdthesis(bibtex_Phdthesis bibtex_phdthesis) {
        this.bibtex_phdthesis = bibtex_phdthesis;
    }
    public bibtex_Article getBibtex_article() {
        return bibtex_article;
    }

    public void setBibtex_article(bibtex_Article bibtex_article) {
        this.bibtex_article = bibtex_article;
    }
    public bibtex_Book getBibtex_book() {
        return bibtex_book;
    }

    public void setBibtex_book(bibtex_Book bibtex_book) {
        this.bibtex_book = bibtex_book;
    }
    public bibtex_Misc getBibtex_misc() {
        return bibtex_misc;
    }

    public void setBibtex_misc(bibtex_Misc bibtex_misc) {
        this.bibtex_misc = bibtex_misc;
    }
    public bibtex_Techreport getBibtex_techreport() {
        return bibtex_techreport;
    }

    public void setBibtex_techreport(bibtex_Techreport bibtex_techreport) {
        this.bibtex_techreport = bibtex_techreport;
    }
    public bibtex_Manual getBibtex_manual() {
        return bibtex_manual;
    }

    public void setBibtex_manual(bibtex_Manual bibtex_manual) {
        this.bibtex_manual = bibtex_manual;
    }
    public bibtex_Conference getBibtex_conference() {
        return bibtex_conference;
    }

    public void setBibtex_conference(bibtex_Conference bibtex_conference) {
        this.bibtex_conference = bibtex_conference;
    }
    public bibtex_Inproceedings getBibtex_inproceedings() {
        return bibtex_inproceedings;
    }

    public void setBibtex_inproceedings(bibtex_Inproceedings bibtex_inproceedings) {
        this.bibtex_inproceedings = bibtex_inproceedings;
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
    public bibtex_Mastersthesis getBibtex_mastersthesis() {
        return bibtex_mastersthesis;
    }

    public void setBibtex_mastersthesis(bibtex_Mastersthesis bibtex_mastersthesis) {
        this.bibtex_mastersthesis = bibtex_mastersthesis;
    }
    public bibtex_Unpublished getBibtex_unpublished() {
        return bibtex_unpublished;
    }

    public void setBibtex_unpublished(bibtex_Unpublished bibtex_unpublished) {
        this.bibtex_unpublished = bibtex_unpublished;
    }

}