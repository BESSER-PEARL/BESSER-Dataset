





import java.util.List;
import java.util.ArrayList;

public class adb_UsePackageClause extends UseClause {






    private List<adb_LibraryUnitDeclaration> adb_libraryunitdeclarations;


    public adb_UsePackageClause(
    ) {
        super(
        );
        this.adb_libraryunitdeclarations = new ArrayList<>();
    }

    public adb_UsePackageClause(
        ArrayList<adb_LibraryUnitDeclaration> adb_libraryunitdeclarations    ) {
        this.adb_libraryunitdeclarations = adb_libraryunitdeclarations;
    }


    public List<adb_LibraryUnitDeclaration> getAdb_libraryunitdeclarations() {
        return adb_libraryunitdeclarations;
    }

    public void addAdb_libraryunitdeclaration(Adb_libraryunitdeclaration adb_libraryunitdeclaration) {
        this.adb_libraryunitdeclarations.add(adb_libraryunitdeclaration);
    }

}