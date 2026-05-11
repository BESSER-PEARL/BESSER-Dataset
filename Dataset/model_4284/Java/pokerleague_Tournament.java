





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Tournament extends DescribedEntity {

    private String tournamentStart;
    private int minPlayers;
    private String tournamentEnd;
    private int defaultBuyIn;
    private int maxPlayers;
    private int tournamentAnnouncementLead;





    private pokerleague_PrizeMoneyRuleSet pokerleague_prizemoneyruleset;




    private pokerleague_Invitation pokerleague_invitation;




    private List<pokerleague_Invitation> pokerleague_invitations;




    private List<pokerleague_Game> pokerleague_games;




    private pokerleague_Game pokerleague_game;


    public pokerleague_Tournament(
        String tournamentStart,        int minPlayers,        String tournamentEnd,        int defaultBuyIn,        int maxPlayers,        int tournamentAnnouncementLead    ) {
        super(
        );
        this.tournamentStart = tournamentStart;
        this.minPlayers = minPlayers;
        this.tournamentEnd = tournamentEnd;
        this.defaultBuyIn = defaultBuyIn;
        this.maxPlayers = maxPlayers;
        this.tournamentAnnouncementLead = tournamentAnnouncementLead;
        this.pokerleague_invitations = new ArrayList<>();
        this.pokerleague_games = new ArrayList<>();
    }

    public pokerleague_Tournament(
        String tournamentStart,        int minPlayers,        String tournamentEnd,        int defaultBuyIn,        int maxPlayers,        int tournamentAnnouncementLead        ArrayList<pokerleague_Invitation> pokerleague_invitations,        ArrayList<pokerleague_Game> pokerleague_games    ) {
        this.tournamentStart = tournamentStart;
        this.minPlayers = minPlayers;
        this.tournamentEnd = tournamentEnd;
        this.defaultBuyIn = defaultBuyIn;
        this.maxPlayers = maxPlayers;
        this.tournamentAnnouncementLead = tournamentAnnouncementLead;
        this.pokerleague_invitations = pokerleague_invitations;
        this.pokerleague_games = pokerleague_games;
    }

    public String getTournamentstart() {
        return tournamentStart;
    }

    public void setTournamentstart(String tournamentStart) {
        this.tournamentStart = tournamentStart;
    }
    public int getMinplayers() {
        return minPlayers;
    }

    public void setMinplayers(int minPlayers) {
        this.minPlayers = minPlayers;
    }
    public String getTournamentend() {
        return tournamentEnd;
    }

    public void setTournamentend(String tournamentEnd) {
        this.tournamentEnd = tournamentEnd;
    }
    public int getDefaultbuyin() {
        return defaultBuyIn;
    }

    public void setDefaultbuyin(int defaultBuyIn) {
        this.defaultBuyIn = defaultBuyIn;
    }
    public int getMaxplayers() {
        return maxPlayers;
    }

    public void setMaxplayers(int maxPlayers) {
        this.maxPlayers = maxPlayers;
    }
    public int getTournamentannouncementlead() {
        return tournamentAnnouncementLead;
    }

    public void setTournamentannouncementlead(int tournamentAnnouncementLead) {
        this.tournamentAnnouncementLead = tournamentAnnouncementLead;
    }

    public pokerleague_PrizeMoneyRuleSet getPokerleague_prizemoneyruleset() {
        return pokerleague_prizemoneyruleset;
    }

    public void setPokerleague_prizemoneyruleset(pokerleague_PrizeMoneyRuleSet pokerleague_prizemoneyruleset) {
        this.pokerleague_prizemoneyruleset = pokerleague_prizemoneyruleset;
    }
    public pokerleague_Invitation getPokerleague_invitation() {
        return pokerleague_invitation;
    }

    public void setPokerleague_invitation(pokerleague_Invitation pokerleague_invitation) {
        this.pokerleague_invitation = pokerleague_invitation;
    }
    public List<pokerleague_Invitation> getPokerleague_invitations() {
        return pokerleague_invitations;
    }

    public void addPokerleague_invitation(Pokerleague_invitation pokerleague_invitation) {
        this.pokerleague_invitations.add(pokerleague_invitation);
    }
    public List<pokerleague_Game> getPokerleague_games() {
        return pokerleague_games;
    }

    public void addPokerleague_game(Pokerleague_game pokerleague_game) {
        this.pokerleague_games.add(pokerleague_game);
    }
    public pokerleague_Game getPokerleague_game() {
        return pokerleague_game;
    }

    public void setPokerleague_game(pokerleague_Game pokerleague_game) {
        this.pokerleague_game = pokerleague_game;
    }

}