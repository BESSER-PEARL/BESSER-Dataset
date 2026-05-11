





import java.util.List;
import java.util.ArrayList;

public class StatementContainer  {






    private cobol_files_FileName cobol_files_filename;




    private cobol_sections_Section cobol_sections_section;




    private cobol_paragraphs_Paragraph cobol_paragraphs_paragraph;




    private cobol_divisions_Division cobol_divisions_division;


    public StatementContainer(
    ) {
    }



    public cobol_files_FileName getCobol_files_filename() {
        return cobol_files_filename;
    }

    public void setCobol_files_filename(cobol_files_FileName cobol_files_filename) {
        this.cobol_files_filename = cobol_files_filename;
    }
    public cobol_sections_Section getCobol_sections_section() {
        return cobol_sections_section;
    }

    public void setCobol_sections_section(cobol_sections_Section cobol_sections_section) {
        this.cobol_sections_section = cobol_sections_section;
    }
    public cobol_paragraphs_Paragraph getCobol_paragraphs_paragraph() {
        return cobol_paragraphs_paragraph;
    }

    public void setCobol_paragraphs_paragraph(cobol_paragraphs_Paragraph cobol_paragraphs_paragraph) {
        this.cobol_paragraphs_paragraph = cobol_paragraphs_paragraph;
    }
    public cobol_divisions_Division getCobol_divisions_division() {
        return cobol_divisions_division;
    }

    public void setCobol_divisions_division(cobol_divisions_Division cobol_divisions_division) {
        this.cobol_divisions_division = cobol_divisions_division;
    }

}