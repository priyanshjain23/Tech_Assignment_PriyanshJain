SELECT StudentName,
               CollegeName,
               Round1Marks,
               Round2Marks,
               Round3Marks,
               TechnicalRoundMarks,
               TotalMarks,
               Result,
               Rank() over (order by TotalMarks Desc) as Rank_Result
                FROM T1;